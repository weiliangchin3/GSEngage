import React from "react";
import ReactSpreadSheet from '../ReactDatasheet/ReactSpreadSheet'
import 'antd/dist/antd.min.css';
import Header from '../headerText/index';;

function Main() {
    return(
        <div>
            <Header/>
            <ReactSpreadSheet/>
        </div>
    )
}

export default Main;