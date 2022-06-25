import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'antd/dist/antd.min.css';
import Main from './components/Main/index';
import ResultURL from './result/index';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


ReactDOM.render(
  <React.StrictMode>
    <Router>
          <Switch>
            <Route path="/" exact component={Main}/>
            <Route path ="/result" component={ResultURL}/>
          </Switch>
      </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
