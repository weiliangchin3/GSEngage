import axios from "axios";

export async function getAllTemplates() {
    return await axios.get('https://jasmine-tan-2019-smu-edu-sg.solutions.apixplatform.com/template/all');
}

export async function getTemplateById({params = {}}) {
    return await axios.get('https://jasmine-tan-2019-smu-edu-sg.solutions.apixplatform.com/template/id=' + params.id);
}

export async function createReportCopy({params = {}}) {
    const meta = await axios.post('https://jasmine-tan-2019-smu-edu-sg.solutions.apixplatform.com/report/save', params )
    return meta
}

export async function generteOwnReport({params = {}}) {
    const meta = await axios.post('https://template-2b4cd56mpa-as.a.run.app/api/v1/templates', JSON.parse(params) )
    return meta
}

export async function getAllReport() {
    return await axios.get('https://jasmine-tan-2019-smu-edu-sg.solutions.apixplatform.com/report/all');
}

export async function getReportById({params = {}}) {
    const meta = await axios.get('https://jasmine-tan-2019-smu-edu-sg.solutions.apixplatform.com/formatter/render', {
        params: {
            ...params
        }
    });

    return meta
}

export async function afterUpload({params = {}}) {
    const meta = await axios.post('https://formatter-container-2b4cd56mpa-as.a.run.app/render/inputs?reportID=' + params.reportID, JSON.parse(params.data));
    return meta
}

export async function downloadExcel({params = {}}) {
    const meta = await axios.post('https://excel-builder-container-2b4cd56mpa-as.a.run.app/download/v2', params.data);
    return meta
}

export async function saveFile({params = {}}) {
    const meta = await axios.put('https://report-2b4cd56mpa-as.a.run.app/update', params.data);

    return meta
}