function renderContent(content) {
    $.ajax({
        type: 'GET',
        url: content,
        data: {},
        success: function (data) {
            $('#content').html(data);
        },
    });
}

function createForm(formId, model, callback) {
    let formData = {};
    $(`#${formId} .form-control`).each(function () {
        formData[$(this).attr('id')] = $(this).val();
    });

    $.ajax({
        type: 'POST',
        url: `http://localhost:5000/${model}/`,
        data: JSON.stringify(formData),
        success: function (response, textStatus, xhr) {
            callback(xhr);
            $(`#${formId} .form-control`).each(function () {
                $(this).val('');
            });
        },
        error: function (response) {
            alert('No se pudo crear el registro');
        }
    });
}

function getData(model, callback) {
    $.ajax({
        type: 'GET',
        url: `http://localhost:5000/${model}/`,
        data: {},
        success: function (response) {
            callback(response);
        },
        error: function (response) {
            callback(response);
        }
    });
}

function getRelatedDataList(model, callback) {
    $.ajax({
        type: 'GET',
        url: `http://localhost:5000/${model}/list_related_data`,
        data: {},
        success: function (response) {
            callback(response);
        },
        error: function (response) {
            callback(response);
        }
    });
}

function getUniqueData(id, model, callback) {
    $.ajax({
        type: 'GET',
        url: `http://localhost:5000/${model}/${id}`,
        data: {},
        success: function (response) {
            callback(response);
        },
        error: function (response) {
            alert('Registro no encontrado');
        }
    });
}

function updateForm(formId, id, model, callback) {
    let formData = {};
    $(`#${formId} .form-control`).each(function () {
        formData[$(this).attr('id')] = $(this).val();
    });

    $.ajax({
        type: 'PUT',
        url: `http://localhost:5000/${model}/${id}`,
        data: JSON.stringify(formData),
        success: function (response, textStatus, xhr) {
            callback(xhr);
            $(`#${formId} .form-control`).each(function () {
                $(this).val('');
            });
        },
        error: function (response) {
            alert('No se pudo actualizar el registro');
        }
    });
}


function deleteData(formId, id, model, callback) {
    $.ajax({
        type: 'DELETE',
        url: `http://localhost:5000/${model}/${id}`,
        data: {},
        success: function (response, textStatus, xhr) {
            callback(xhr);
            $(`#${formId} .form-control`).each(function () {
                $(this).val('');
            });
        },
        error: function (response) {
            alert('No se pudo eliminar el registro');
        }
    });
}

$(document).ready(() => renderContent('paginas/horario/list.html'));
