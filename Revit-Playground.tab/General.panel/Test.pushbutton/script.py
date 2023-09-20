# -*- coding: utf-8 -*-

# Importar los módulos necesarios
import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector, Transaction

# Obtener los servicios de Revit
from pyrevit import revit, DB
from pyrevit import script
__author__ = "[Tu Nombre]"

# Obtener el documento activo y la vista activa
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
view = uidoc.ActiveView

class CategorySelectionFilter(ISelectionFilter):
    def AllowElement(self, element):
        # Asegúrate de que la categoría esté escrita correctamente y coincida con la de tu modelo
        return element.Category.Name == "Structural Foundations"  # Cambiado a "Structural Foundations" si es el nombre correcto

    def AllowReference(self, reference, point):
        return True

# Define un filtro para seleccionar elementos de la categoría "Structural Foundations"
filter = CategorySelectionFilter()

try:
    # Utiliza el método PickObjects para permitir al usuario seleccionar elementos.
    picked_elements = uidoc.Selection.PickObjects(ObjectType.Element, filter, "Selecciona elementos de la categoría 'Structural Foundations'")
    
    if picked_elements:
        # Recopila los ElementId de los elementos seleccionados
        selected_element_ids = [reference.ElementId for reference in picked_elements]

        # Convierte la lista de ElementId en una colección List[ElementId]
        selected_element_ids_collection = List[ElementId](selected_element_ids)

        # Establece los elementos seleccionados en el documento actual
        uidoc.Selection.SetElementIds(selected_element_ids_collection)

        # Ahora los elementos permanecerán seleccionados y puedes manipularlos posteriormente
    else:
        # No se seleccionaron elementos.
        TaskDialog.Show("Sin selección", "No se seleccionaron elementos de la categoría 'Structural Foundations'.")
except OperationCanceledException:
    # El usuario presionó el botón "Escape" para cancelar la selección.
    TaskDialog.Show("Selección cancelada", "El usuario canceló la selección de elementos.")
