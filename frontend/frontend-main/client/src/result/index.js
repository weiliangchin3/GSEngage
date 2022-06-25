import react, {useState, useEffect} from "react";
import { Result, Button } from 'antd';
import { useHistory, useLocation } from "react-router-dom";


function ResultURL() {
    let history = useHistory();
    const location = useLocation();
    const [url, setUrl] = useState('');

    useEffect(() => {
        setUrl(location.state.data.url)
     }, [location]);
    return(
        <Result
            status="success"
            title="Successfully Converted to Excel"
            subTitle={<a href={url}>Click here to download Excel</a>}
            extra={[
            <Button type="primary" key="console" onClick={() =>history.push("/")}>
                Back to HomePage
            </Button>
            ]}
        />
    )
}
export default ResultURL;
