import os
import xml.dom.minidom as dom
from pathlib import Path
from classes.energy_controlling import EnergyControlling
from classes.smart_home import SmartHome
from classes.energy_consumption_appliance import EnergyConsumingAppliance
from classes.energy_source import EnergySource
from ontology.onto_api import OntologyAPI


class LoadXML():

    def doit(self):
        print('here to do so')
        ontAPI = OntologyAPI()
        print('loaded api')

        #get xml
        xml_path = os.path.join(os.path.dirname(__file__), "smarthome.xml" )
        baum = dom.parse(xml_path)
        print('xml loaded')

        #get all instances
        instances = baum.getElementsByTagName("instance")
        connectors = baum.getElementsByTagName("connector")

        #get model instance
        model = baum.getElementsByTagName("model")
        modelinstance = SmartHome()
        modelinstance.setsmarthome(model)

        #add text to id, because ontology dont likes integer and special charakters
        idplustext = "id" + modelinstance.id
        print(idplustext)
        ontAPI.setclassprosumer(idplustext, "Joseph Volt", "Faster than Bolt", "secret", "0xc6s4df5s64d1cfs300")
        print("saved class prosumer to ontology")
        modelinstance.getsmarthome()


        for instance in instances:

            idpara = instance.getAttribute("id")
            namepara = instance.getAttribute("name")

            if instance.getAttribute("class") == "Energy Controlling":
                ec = EnergyControlling()
                ec.setenergycontrolling(idpara, namepara, instance)
                #replace all blanks an hyphen
                nameNoBlank = ec.name.replace(" ","")
                nameNoBlankHyphen = nameNoBlank.replace("-","")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergycontrolling(ec.id, nameNoBlankHyphen, ec.type, ec.description, ec.systemType, ec.counter, ec.task)
                print("saved class Energy_Controlling to ontology")
                ec.getenergycontrolling()

            if instance.getAttribute("class") == "Energy Consuming Appliances":
                eca = EnergyConsumingAppliance()
                eca.setenergyconsuminappliance(idpara, namepara, instance)
                #def setclassenergyconsumingappliances(self, onto, id, name, type, description, Power_Consuming_Maximum, Power_Consuming_Average, Power_Consuming_Current, Consuming_Begin, Consuming_End, Active):
                #replace all blanks an hyphen
                nameNoBlank = eca.name.replace(" ","")
                nameNoBlankHyphen = nameNoBlank.replace("-","")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergyconsumingappliances(eca.id, nameNoBlankHyphen, eca.type, eca.description, eca.powerConsumingMaximum, eca.powerConsumingAverage, eca.powerConsumingCurrent, eca.consumingBegin, eca.consumingEnd, eca.active)
                print("saved class Energy_Consuming Appliances to ontology")           
                eca.getenergyconsumingappliance()

            if instance.getAttribute("class") == "Energy Source":
                es = EnergySource()
                #def setclassenergysource(self, onto, id, name, type, description, Power_Supplying_Maximum, Power_Supplying_Average, Power_Supplying_Current, Supplying_Begin, Supplying_End, Power_Production_Maximum, Power_Production_Average, Power_Production_Current, Production_Begin, Production_End):
                es.setenergysource(idpara, namepara, instance)
                #replace all blanks an hyphen
                nameNoBlank = es.name.replace(" ","")
                nameNoBlankHyphen = nameNoBlank.replace("-","")
                print("++++++++++" + nameNoBlankHyphen)
                ontAPI.setclassenergysource(es.id, nameNoBlankHyphen, es.type, es.description, es.powerSupplyingMaximum, es.powerSupplyingAverage, es.powerSupplyingCurrent, es.supplyingBegin, es.supplyingEnd, es.powerProductionMaximum, es.powerProductionAverage, es.powerProductionCurrent, es.productionBegin, es.productionEnd, es.active)
                print("saved class Energy_Source to ontology")
                es.getenergysource()
        

