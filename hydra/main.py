import hydra
from omegaconf import OmegaConf, DictConfig

@hydra.main(config_name="config.yaml", config_path="./configs")
def main(cfg: DictConfig) -> None:
    # Print the config file using `to_yaml` method which prints in a pretty manner
    print(OmegaConf.to_yaml(cfg))
    print("="*50)
    print(cfg.model.tokenizer, cfg.processing.batch_size, cfg.processing.max_length)


if __name__ == "__main__":
    main()
