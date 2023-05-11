from abc import abstractmethod

import boaviztapi.utils.roundit as rd
from boaviztapi.model import ComputedImpacts
from boaviztapi.model.boattribute import Boattribute
from boaviztapi.model.usage import ModelUsage
from boaviztapi.service.archetype import get_arch_value, get_arch_component


class Component:
    NAME = "COMPONENT"

    def __init__(self, archetype=None, **kwargs):
        self.impact_factor = {}
        self.archetype = archetype
        self.units = Boattribute(
            default=get_arch_value(archetype, 'units', 'default', default=1),
            min=get_arch_value(archetype, 'units', 'min'),
            max=get_arch_value(archetype, 'units', 'max')
        )
        self._usage = None

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    @property
    def usage(self) -> ModelUsage:
        if self._usage is None:
            self._usage = ModelUsage(archetype=get_arch_component(self.archetype,"USAGE"))
        return self._usage

    @usage.setter
    def usage(self, value: int) -> None:
        self._usage = value

    def impact_use(self, impact_type: str) -> ComputedImpacts:
        if not self.usage.hours_electrical_consumption.is_set():
            raise NotImplementedError
        impact_factor = self.usage.elec_factors[impact_type]

        impacts = impact_factor.value * (
                self.usage.hours_electrical_consumption.value / 1000) * self.usage.use_time.value
        sig_fig = self.__compute_significant_numbers_usage(impact_factor.value)

        max_impact = impact_factor.max * (self.usage.hours_electrical_consumption.max / 1000) * self.usage.use_time.max
        min_impact = impact_factor.min * (self.usage.hours_electrical_consumption.min / 1000) * self.usage.use_time.min


        return impacts, sig_fig, min_impact, max_impact, []

    def __compute_significant_numbers_usage(self, impact_factor: float) -> int:
        return rd.min_significant_figures(self.usage.hours_electrical_consumption.value, self.usage.use_time.value,
                                          impact_factor)

    @abstractmethod
    def impact_embedded(self, impact_type: str) -> ComputedImpacts:
        raise NotImplementedError