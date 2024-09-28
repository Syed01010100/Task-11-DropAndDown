""""
Testing - Drop and Down (https://jqueryui.com/droppable/)
"""


from Dropanddown_Action import DragAndDrop
import pytest


url="https://jqueryui.com/droppable/"
Syed=DragAndDrop(url)

def test_get_url():
    assert Syed.open_url() == True
    print("Success: Automation of webpage has started")


def test_iframe():
    assert Syed.switch_to_iframe() == True
    print("Success")


def test_drag_drop():
    assert  Syed.perform_drag_and_drop() == None
    print("Success:Drag and Drop has performed")

