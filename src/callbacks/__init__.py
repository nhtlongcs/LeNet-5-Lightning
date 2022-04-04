from registry import Registry

CALLBACKS_REGISTRY = Registry("CALLBACKS")

from pytorch_lightning.callbacks import (
    ModelCheckpoint,
    LearningRateMonitor,
    EarlyStopping,
)

CALLBACKS_REGISTRY.register(LearningRateMonitor)
CALLBACKS_REGISTRY.register(EarlyStopping)
CALLBACKS_REGISTRY.register(ModelCheckpoint)
