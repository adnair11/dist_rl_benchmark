import gradio as gr




def display_choice(algo, game,slider):
    # # Dictionary to store mean scores for each algorithm and game
    # if algo == "C51" and game == "Pong":
    #     mean_scores = test_c51()
    #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "FQF" and game == "Pong":
    
    #     config_fqf["task"] = "PongNoFrameskip-v4"
    #     config_fqf["resume_path"] = "fqf_pong.pth"
    #     mean_scores = test_FQF(config_fqf)
    #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "FQF" and game == "Space Invaders":
        
    #     config_fqf["task"] = "SpaceInvadersNoFrameskip-v4"
    #     config_fqf["resume_path"] = "Spaceinv_FQF.pth"
    #     mean_scores = test_FQF(config_fqf)
    #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "FQF" and game == "Freeway":
    #     config_fqf["seed"] = slider
    #     config_fqf["task"] = "FreewayNoFrameskip-v4"
    #     config_fqf["resume_path"] = "examples/atari/fqf_freeway.pth"
    #     mean_scores = test_FQF(config_fqf)
    #     mean_scores = mean_scores.returns_stat.mean

    # if algo == "FQF" and game == "MsPacman":
    #     config_fqf["seed"] = slider
    #     config_fqf["task"] = "MsPacmanNoFrameskip-v4"
    #     config_fqf["resume_path"] = "fqf_pacman.pth"
    #     mean_scores = test_FQF(config_fqf)
    #     mean_scores = mean_scores.returns_stat.mean

    # # if algo == "FQF" and game == "Tennis":
    # #     config_fqf["seed"] = slider
    # #     config_fqf["task"] = "TennisNoFrameskip-v4"
    # #     config_fqf["resume_path"] = "fqf_tennis.pth"
    # #     mean_scores = test_FQF(config_fqf)
    # #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "C51" and game == "Freeway":
    #     config["seed"] = slider
    #     config["task"] = "FreewayNoFrameskip-v4"
    #     config["resume_path"] = "c51_freeway.pth"
    #     mean_scores = test_c51()
    # if algo == "C51" and game == "MsPacman":
    #     config["seed"] = slider
    #     config["task"] = "MsPacmanNoFrameskip-v4"
    #     config["resume_path"] = "c51_pacman.pth"
    #     mean_scores = test_c51()
    #     mean_scores = mean_scores.returns_stat.mean
    # # if algo == "C51" and game == "Tennis":
    # #     config["seed"] = slider
    # #     config["task"] = "TennisNoFrameskip-v4"
    # #     config["resume_path"] = "c51_tennis.pth"
    # #     mean_scores = test_c51()
    # #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "FQF-Rainbow" and game == "Freeway":
    #     config_fqf_r["seed"] = slider
    #     config_fqf_r["task"] = "FreewayNoFrameskip-v4"
    #     config_fqf_r["resume_path"] = "fqf-rainbow_freeway.pth"
    #     mean_scores = test_fqf_rainbow(config_fqf_r)
    #     mean_scores = mean_scores.returns_stat.mean
    # if algo == "FQF-Rainbow" and game == "MsPacman":
    #     config_fqf_r["seed"] = slider
    #     config_fqf_r["task"] = "MsPacmanNoFrameskip-v4"
    #     config_fqf_r["resume_path"] = "fqf_rainbow_pacman.pth"
    #     mean_scores = test_fqf_rainbow(config_fqf_r)
    #     mean_scores = mean_scores.returns_stat.mean


    
        mean_scores = {
            ("C51", "Pong"): 20.5,
            ("C51", "Space Invaders"): 1500,
            ("FQF", "Pong"): 21.0,
            ("FQF", "Space Invaders"): 1600,
            ("FQF-Rainbow", "Pong"): 21.0,
            ("FQF-Rainbow", "Space Invaders"): 1700,
        }

        # Calculate or fetch the mean score for the selected combination
        mean_score = mean_scores.get((algo, game), "No data available")

        # Return the selected options and the mean score
        return f"Your {algo} agent finished {game} with a \nMean Score of  ##{mean_score}"
    # return [mean_scores,"video-app/rl-video-episode-0.mp4"]

# Define the choices for the radio buttons
algos = ["C51", "FQF", "FQF-Rainbow"]
games = ["Pong", "Space Invaders","Freeway","MsPacman"]






demo = gr.Interface(
    fn=display_choice,          # Function to call when an option is selected
    inputs=[gr.Radio(algos,label="Algorithm"), gr.Radio(games, label="Game"),gr.Slider(maximum=100,label="Seed")],   # Radio buttons with the defined choices
    # outputs=[gr.Textbox(label="Score"),gr.Video(autoplay=True,height=480,width=480,label="Replay")],
    outputs=[gr.Textbox(label="Score")],
    title="Distributional RL Algorithms Benchmark",
    description="Select the DRL agent and the game of your choice",
    theme="soft",
    examples=[["FQF","Pong",31],
              ["C51","Space Invaders",31],
              ["FQF-Rainbow","Freeway",31]
              ]
)


if __name__ == "__main__":
    demo.launch(share=False)
