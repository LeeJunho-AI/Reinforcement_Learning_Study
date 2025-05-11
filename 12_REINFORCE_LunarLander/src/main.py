import torch
import gymnasium as gym
from policy import PolicyNetwork
from utils import compute_returns
import numpy as np
import matplotlib.pyplot as plt
import os

LEARNING_RATE = 1e-3
EPISODES = 1000
MAX_STEPS = 1000
PRINT_EVERY = 10
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
VIDEO_PATH = os.path.join(BASE_DIR, 'results/')
MODEL_PATH = os.path.join(BASE_DIR, 'results', 'best_model.pth')

# results 디렉토리 생성
os.makedirs(VIDEO_PATH, exist_ok=True)

def train(env):
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    policy = PolicyNetwork(state_dim, action_dim)
    optimizer = torch.optim.Adam(policy.parameters(), lr=LEARNING_RATE)
    episode_rewards = []
    best_reward = -float('inf')

    for episode in range(EPISODES):
        state, _ = env.reset()
        log_probs = []
        rewards = []
        total_reward = 0

        for _ in range(MAX_STEPS):
            state_tensor = torch.FloatTensor(np.array(state))
            action_probs = policy(state_tensor)
            action_dist = torch.distributions.Categorical(action_probs)
            action = action_dist.sample()
            log_prob = action_dist.log_prob(action)

            next_state, reward, done, _, _ = env.step(action.item())
            log_probs.append(log_prob)
            rewards.append(reward)
            total_reward += reward
            state = next_state

            if done:
                break

        returns = compute_returns(rewards)
        loss = -torch.sum(torch.stack(log_probs) * returns)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 모델 저장 로직 추가
        if total_reward > best_reward:
            best_reward = total_reward
            torch.save(policy.state_dict(), MODEL_PATH)
            print(f"[+] New best model saved with reward: {best_reward}")

        episode_rewards.append(total_reward)
        if episode % PRINT_EVERY == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}, Average Reward: {np.mean(episode_rewards[-PRINT_EVERY:])}")

    return episode_rewards


def plot_rewards(rewards):
    plt.plot(rewards)
    plt.title('REINFORCE Training Rewards')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.savefig('results/training_rewards.png')
    plt.show()


def record_video(env, policy, video_length=1000):
    # 영상 녹화를 위한 환경 생성
    env = gym.make('LunarLander-v3', render_mode='rgb_array')
    obs, _ = env.reset()
    
    frames = []
    for _ in range(video_length):
        action_probs = policy(torch.FloatTensor(np.array(obs)))
        action_dist = torch.distributions.Categorical(action_probs)
        action = action_dist.sample()
        obs, _, done, _, _ = env.step(action.item())
        
        # 현재 프레임 저장
        frame = env.render()
        frames.append(frame)
        
        if done:
            break
    
    # 영상 저장
    import imageio
    video_path = os.path.join(VIDEO_PATH, 'best_model_episode.mp4')
    imageio.mimsave(video_path, frames, fps=30)
    print(f"[+] 영상이 저장되었습니다: {video_path}")
    
    env.close()


# 단일 환경 학습
env = gym.make('LunarLander-v3')
rewards = train(env)
plot_rewards(rewards)
env.close()

# 모델 불러와서 영상 녹화
policy = PolicyNetwork(env.observation_space.shape[0], env.action_space.n)
policy.load_state_dict(torch.load(MODEL_PATH))
record_video(env, policy)