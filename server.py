import os
import uuid
from flask import render_template, request, redirect, url_for

import connexion

basedir = os.path.abspath(os.path.dirname(__file__))

app = connexion.App(__name__, specification_dir=basedir)

app.add_api('swagger.yml')


def get_files(my_path):
    return [f for f in os.listdir(
        my_path) if os.path.isfile(os.path.join(my_path, f))]


def generate_images():

    my_path = './images/dest'
    # dest_path = my_path + '/dest'

    images = get_files(my_path)

    for image in images:
        full_name = os.path.basename(image)
        fname, ext = os.path.splitext(full_name)
        new_name = uuid.uuid4()
        os.rename(os.path.join(my_path, full_name),
                  os.path.join(my_path, str(new_name) + ext.lower()))

    return get_files(my_path)


@app.route('/')
def home():
    """

    """

    return render_template('home.html')


@app.route('/api')
def api():
    """
    This function just responds to the browser URL http://localhost:5000/
    :return: the rendered template home.html
    """

    # read all the image files then render home.html with that list
    # build a list and populate a form to create all the properties for each file

    # print(images)

    return render_template('api.html')
    # return "hi there"


@app.route('/reportage')
def reportage():
    """
    """

    return render_template('reportage.html')


@app.route('/search')
def search():
    """
    """

    return render_template('search.html')


@app.route('/about')
def about():
    """
    """

    return render_template('about.html')


@app.route('/projects')
def projects():
    """
    """

    return render_template('projects.html')


@app.route('/admin/populate_db')
def populate_db():
    # images = generate_images()
    files_path = './images/dest'
    images = get_files(files_path)

    return render_template('populatedb.html', images=images)


@app.route('/admin/update')
def update_image(image):
    """
    update image properties
    """

    return


@app.route('/gallery')
def gallery():
    print(request.args.get('filename'))
    return render_template(request.args.get('filename'))


# if we are running in standalone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
