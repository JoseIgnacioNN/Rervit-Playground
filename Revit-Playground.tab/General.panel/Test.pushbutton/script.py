# -*- coding: utf-8 -*-

# BIBLIOTECAS
# ............................................................................
import clr

from pyrevit import PyRevitException, PyRevitIOError


# Agregar las referencias de Autodesk.Revit.DB y Autodesk.Revit.UI desde pyRevit
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
from Autodesk.Revit.Exceptions import *

# Para trabajar con ICollection
from System.Collections.Generic import List

# Para trabajar contra el documento y hacer transacciones
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

class CategorySelectionFilter(ISelectionFilter):
	def AllowElement(self, element):
		# Asegúrate de que la categoría esté escrita correctamente y coincida con la de tu modelo
		return element.Category.Name == "Structural Foundations"  # Cambiado a "Structural Foundations" si es el nombre correcto

	def AllowReference(self, reference, point):
		return True

# Define un filtro para seleccionar elementos de la categoría "Structural Foundations"
filter = CategorySelectionFilter()

# Utiliza el método PickObjects para permitir al usuario seleccionar elementos.
picked_elements = uidoc.Selection.PickObjects(ObjectType.Element, filter, "Selecciona elementos de la categoría 'Structural Foundations'")

try:
    if picked_elements:
        # Recopila los ElementId de los elementos seleccionados
        selected_element_ids = [reference.ElementId for reference in picked_elements]

        # Convierte la lista de ElementId en una colección List[ElementId]
        selected_element_ids_collection = List[ElementId](selected_element_ids)

        # Establece los elementos seleccionados en el documento actual
        uidoc.Selection.SetElementIds(selected_element_ids_collection)

        # Ahora los elementos permanecerán seleccionados y puedes manipularlos posteriormente
    else:
        # El usuario canceló la selección o no se seleccionaron elementos.
        TaskDialog.Show("Sin selección", "No se seleccionaron elementos de la categoría 'Structural Foundations'.")

except OperationCanceledException:
    # Maneja la excepción si el usuario la cancela
    print("kfjahgsdkjfha")