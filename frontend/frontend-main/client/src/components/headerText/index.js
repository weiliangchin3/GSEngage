import React from 'react';
import { Typography } from 'antd';
import { header } from '../constants/constants';
import './index.css';
import 'antd/dist/antd.min.css';

const { Title } = Typography;

function Header() {
    return (
        <div className='header'>
            <Title>{header}</Title>
        </div>
    )
}

export default Header;
