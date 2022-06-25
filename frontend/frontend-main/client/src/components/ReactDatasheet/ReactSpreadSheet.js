import React, {useState, useEffect} from "react";
import './style.css';
import {Spreadsheet} from "react-spreadsheet";
import { Button, Upload, Modal, Radio, Menu, Dropdown, message} from 'antd';
import {getAllTemplates, getTemplateById,createReportCopy,getAllReport, getReportById, afterUpload, downloadExcel, saveFile, generteOwnReport} from '../../service/index';
import { matrix} from '../constants/constants';
import { AiOutlineAlignLeft, AiOutlineAlignCenter, AiOutlineAlignRight } from 'react-icons/ai';
import {BsTypeBold} from 'react-icons/bs';
import { useHistory } from "react-router-dom";


const ReactSpreadSheet = () => {
  const [data, setData] = useState(matrix());
  const [select, setSelect] = useState([]);
  const [selected, setSelected] = useState([]);
  const [isModalVisible, setIsModalVisible] = useState(true);
  const [value, setValue] = useState(0);
  const [template, setTemplates] = useState([]);
  const [report, setReport] = useState([]);
  const [selectedReport, setSelectedReport] = useState();
  const [reportDetails, setReportDetails] = useState();
  const [selectedTemplate, setSelectedTemplate] = useState();
  const [reportId, setReportId] = useState();
  const [type, setType] = useState('template');
  const [filename, setFileName] = useState('');
  const [reportName, setReportName] = useState('');
  const [templateName, setTemplateName] = useState('');
  let history = useHistory();

  async function fetchData() {
    const all_templates = await getAllTemplates();
    setTemplates(all_templates.data);
    const all_report = await getAllReport();
    setReport(all_report.data);
  };

  useEffect(() => {
      fetchData()
  }, []);

  async function getTemplate(selectedTemplate) {
    const result = await getTemplateById({
      params: {
          id: selectedTemplate
      },
    });
    createReport(result.data)
  };

  async function getReport(selectedReport) {
    const result = await getReportById({
      params: {
          reportID: selectedReport
      },
    });
    setReportDetails(result.data)
    setData(result.data.sheets[0].rows)
    setReportId(result.data.reportId)
  };

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleOk = () => {
    if (type === 'template') {
      getTemplate(selectedTemplate)
    } else if (type === 'report') {
      getReport(selectedReport)
    } else{
      getTemplate(selectedTemplate)
    }
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  async function createReport(details) {
    const result = await createReportCopy({
      params: {
          'reportName': details['reportName'],
          'sheets' : details['sheets'],
          'templateId': details['templateId'],
          'templateName': details['templateName']
      }
    });
    getReport(result.data)
  };


  function HandleCellChange(color) {
    if (color.includes('highlight')) {
      var search= "highlight";
    } else if (color.includes('text')) {
      var search= "text";
    } else if (color.includes('align')) {
      var search = 'align'
    } else if (color.includes('bold')) {
      var search = 'bold'
    }
    const newMatrix = JSON.parse(JSON.stringify(data));
    for (let i=0; i<selected.length; i++) {
      const newClassName = newMatrix[selected[i].row][selected[i].column].className
      const classname_split = newClassName.split(" ");
      if (newClassName.includes(search) && search !== 'bold'){
        var index = classname_split.findIndex(el => el.includes(search));
        classname_split[index] = color
        newMatrix[selected[i].row][selected[i].column].className = classname_split.join(' ')
      } else if (newClassName.includes(search) && search === 'bold'){
        var index = classname_split.findIndex(el => el.includes(search));
        classname_split.splice(index, 1)
        newMatrix[selected[i].row][selected[i].column].className = classname_split.join(' ')
      } else {
        newMatrix[selected[i].row][selected[i].column].className += " " + color;
      }
    }
    setSelected([]);
    setData(newMatrix);
  }

  async function handleJSONUpload(e){
    const newData = JSON.parse(JSON.stringify(e));
    const result = await generteOwnReport({
      params: newData
    });
    setSelectedTemplate(result.data)
  };

  async function handleSubmission(e){
    const result = await afterUpload({
      params: {
          'reportID': reportId,
          data: e
      }
    });
    setData(result.data.sheets[0].rows)
  };

  useEffect(() => {
    for (let i=0; i<select.length; i++) {
      setSelected([...selected, select[i]])
    }
  }, [select])


  const handleSetTemplate = (e) => {
    setSelectedTemplate(e.key)
  }

  const handleSetReport = (e) => {
    setSelectedReport(e.key)
  }

  const templateMenu = (
    <Menu onClick={(e) => handleSetTemplate(e)}>
      {Object.keys(template).map((keyName, i) => {
        return (
          <Menu.Item key={template[keyName]['templateId']} value={template[keyName]} onClick={()=> setTemplateName(template[keyName]['templateName'])}>
              {template[keyName]['templateName']}
          </Menu.Item>
        )
      })}
    </Menu>
  );

  const reporMenu = (
    <Menu onClick={(e) => handleSetReport(e)}>
      {Object.keys(report).map((keyName, i) => {
        return (
          <Menu.Item key={report[keyName]['reportId']} value={report[keyName]} onClick={()=> setReportName(report[keyName]['reportName'])}>
              {report[keyName]['reportName']}
          </Menu.Item>
        )
      })}
    </Menu>
  );

  const chooseType = (e) => {
    setValue(e.target.value)
    if (e.target.value === 0) {
      setType('template')
    } else if (e.target.value === 1){
      setType('report')
    } else {
      setType('own')
    }
  }

  async function UploadtoExcel() {
    const newData = JSON.parse(JSON.stringify(data));
    const newReportDetails = JSON.parse(JSON.stringify(reportDetails));
    newReportDetails.sheets[0].rows = newData
    const result = await downloadExcel({
      params: {
          data: newReportDetails
      }
    });
    if (result.status === 200){
      history.push({
        pathname:"/result",
        state: {data: result.data}})
    }
  }

  async function SaveReport() {
    const newData = JSON.parse(JSON.stringify(data));
    const newReportDetails = JSON.parse(JSON.stringify(reportDetails));
    newReportDetails.sheets[0].rows = newData
    const result = await saveFile({
      params: {
          data: newReportDetails
      }
    });
    if (result.status === 200){
      message.success('Report is successfully saved!',[7]);
    }
  }

  return (
    <div>
      <div style={{display:'flex'}} className="uploadButton">
        <div>
          <Button type="primary" onClick={showModal} >
            Restart
          </Button>
          <Modal title="Choose template or report to start" visible={isModalVisible} onOk={handleOk} onCancel={handleCancel}>
            <Radio.Group value={value} onChange={chooseType}>
              <div style={{marginBottom:'20px'}}>
                  <Radio value={0}>
                    Select Template
                  </Radio>
                  <Dropdown overlay={templateMenu} placement="bottomLeft">
                    <Button>Choose</Button>
                  </Dropdown>
                  { templateName!== '' ? (
                    <h6>{templateName}</h6>
                  ): ''}
              </div>
              <div  style={{marginBottom:'20px'}}>
                <Radio value={1}>
                  Select Report
                </Radio>
                <Dropdown overlay={reporMenu} placement="bottomLeft">
                  <Button>Choose</Button>
                </Dropdown>
                { reportName!== '' ? (
                    <h6>{reportName}</h6>
                  ): ''}
              </div>
              <div>
                <Radio value={2}>
                  Upload Template - JSON file
                </Radio>
                <Upload
                    accept=".json"
                    showUploadList={false}
                    beforeUpload={file => {
                        const reader = new FileReader();
                        reader.onload = e => {
                          handleJSONUpload(e.target.result);
                          setFileName(file.name)
                        };
                        reader.readAsText(file);

                        return false;
                    }}
                >
                    <Button>
                        Click to Upload
                    </Button>
                </Upload>
                { filename !== '' ? (
                  <h5>{filename}</h5>
                ) : ''}
              </div>
            </Radio.Group>
          </Modal>
        </div>
        <div>
          <Upload
              accept=".json"
              showUploadList={false}
              beforeUpload={file => {
                  const reader = new FileReader();
                  reader.onload = e => {
                    handleSubmission(e.target.result);
                  };
                  reader.readAsText(file);

                  return false;
              }}
          >
              <Button>
                  Click to Upload JSON files
              </Button>
          </Upload>
        </div>
      </div>
      <div className="toolbox">
        <div className="text_styling style_container">
          <div className="styling_header">
            Bold Text
          </div>
          <div className="text_styling_box"  onClick={() => HandleCellChange('bold')}>
            <BsTypeBold size={20}/>
          </div>
        </div>
        <div className="text_styling style_container">
          <div className="styling_header">
            Text Alignment
          </div>
          <div className="text_styling_container">
            <div className="text_styling_box" onClick={() => HandleCellChange('left_align')}>
              <AiOutlineAlignLeft size={20}/>
            </div>
            <div className="text_styling_box" onClick={() => HandleCellChange('center_align')}>
              <AiOutlineAlignCenter size={20}/>
            </div>
            <div className="text_styling_box" onClick={() => HandleCellChange('right_align')}>
              <AiOutlineAlignRight size={20}/>
            </div >
          </div>
        </div>
        <div className="style_container">
          <div className="styling_header">
            Highlighter
          </div>
          <div>
            <div className="yellow_highlight circle" onClick={() => HandleCellChange('yellow_highlight')}/>
            <div className="blue_highlight circle" onClick={() => HandleCellChange('blue_highlight')} />
            <div className="green_highlight circle" onClick={() => HandleCellChange('green_highlight')}/>
            <div className="red_highlight circle" onClick={() => HandleCellChange('red_highlight')}/>
          </div>
        </div>
        <div className="style_container">
          <div className="styling_header">
            Text Colour
          </div>
          <div>
            <div className="yellow_highlight circle" onClick={() => HandleCellChange('yellow_text')}/>
            <div className="blue_highlight circle" onClick={() => HandleCellChange('blue_text')} />
            <div className="green_highlight circle" onClick={() => HandleCellChange('green_text')}/>
            <div className="red_highlight circle" onClick={() => HandleCellChange('red_text')}/>
            <div className="black_hightlight circle" onClick={() => HandleCellChange('black_text')}/>
          </div>
        </div>
      </div>
      <div className="spreadsheet_wrapper"> 
        <Spreadsheet className="spreadsheet" data={data} onChange={setData} dragging={true} onSelect={setSelect}/>    
      </div>
      <div>
        <div className="button_group">
          <Button className="button_class" onClick={()=>UploadtoExcel()}>
            Download as Excel File
          </Button>
          {/* <Button className="button_class" onClick={()=>SaveReport()}>
            Save Changes
          </Button> */}
        </div>
      </div>
    </div>
  );
};
export default ReactSpreadSheet;