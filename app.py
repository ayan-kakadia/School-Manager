from controller.main import Controller
from models.main import Model
from view.main import View


def app():
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.start()


if __name__ == "__main__":
    app()
