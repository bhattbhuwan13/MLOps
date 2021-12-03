import hydra
from omegaconf import OmegaConf, DictConfig

@hydra.main(config_name="config.yaml", config_path=".")
def main(cfg: DictConfig) -> None:
    # Print the config file using `to_yaml` method which prints in a pretty manner
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    main()
