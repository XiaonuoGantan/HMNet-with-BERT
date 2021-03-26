import click
import signal
import toml

from hmnet_with_bert.base import MODE_TRAIN, MODE_EVAL


# enable attaching from PDB; use 'kill -10 PID' to enter the debugger
def handle_pdb(_, frame):
    import pdb; pdb.Pdb().set_trace(frame)


signal.signal(signal.SIGUSR1, handle_pdb)


@click.command()
@click.option("--config", "-c", default=None, required=False)
@click.argument("mode")
def run(config: str, mode: str):
    """Main entry-point to run a training or evaluation of the HMNet model with various config
    :param config: config.toml that specifies all or some of the params for the training/evaluation
    :param mode: mode of the run which can be either 'train' or 'eval'
    """
    with open(config, "r") as fp:
        conf = toml.load(fp)

    if mode == MODE_TRAIN:
        raise NotImplementedError
    elif mode == MODE_EVAL:
        raise NotImplementedError
    raise ValueError(f"Mode={mode} is not supported. Abort")


if __name__ == "__main__":
    run()
