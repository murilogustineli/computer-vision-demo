import os
import numpy as np
import matplotlib.pyplot as plt

# Saved models path
def ensure_saved_models_dir_exists():
    """
    Checks if the saved_models directory exists, and creates it if it does not.
    """
    saved_models_dir = './saved_models'
    if not os.path.exists(saved_models_dir):
        os.makedirs(saved_models_dir)

# Plotting
def plot_loss_curves(train_losses, val_losses):
    fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=120)
    fig.suptitle("Training and Validation Loss Over Epochs", fontsize=14, weight='bold')
    ax.plot(train_losses, linewidth=2, label='Training Loss')
    ax.plot(val_losses, linewidth=2, label='Validation Loss')
    ax.set_xticks(np.arange(0, len(train_losses), 1))
    ax.set_xlabel('Epochs')
    ax.set_ylabel('Loss')
    ax.grid(color='blue', linestyle='--', linewidth=1, alpha=0.2)
    ax.legend(loc="upper right")
    spines = ['top', 'right', 'bottom', 'left']
    for s in spines:
        ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.7)
    plt.show()
