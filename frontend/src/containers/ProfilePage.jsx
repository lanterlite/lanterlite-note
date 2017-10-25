import React from 'react';
//---------------------importing components needed in page---------------------

//--------------------importing material-ui components
import FlatButton from 'material-ui/FlatButton';
import {Link} from 'react-router-dom';
import RaisedButton from 'material-ui/RaisedButton';
import Card from 'material-ui/Card';
import TextField from 'material-ui/TextField';
import Dialog from 'material-ui/Dialog';
//-----------------------importing icon-----------------
import Edit from 'material-ui/svg-icons/editor/mode-edit';
import Done from 'material-ui/svg-icons/action/done';
import Delete from 'material-ui/svg-icons/action/delete';
import Upload from 'material-ui/svg-icons/file/file-upload';
import Back from 'material-ui/svg-icons/navigation/chevron-left';
//------import dropzone for uploading file ----------------
import Dropzone from 'react-dropzone';
import axios from 'axios';
import { Redirect } from 'react-router'
import Paper from 'material-ui/Paper'
import Breadcrumb from 'react-breadcrumb';
import BaseContainer from '../components/base_components/Header';
import profileImage from '../assets/dummy/profile-image.jpg'

export default class LoginPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            user: []
        };
    }
	
    /**
     * Get all master data from server
     */
    getData = () => {
        const self = this
        var url = this.props.url.site + this.props.url.backendRoute.version + this.props.url.backendRoute.user + '/1'
        axios.get(url).then(function(request){
            let stateCopy = Object.assign({}, self)
            stateCopy.state.user = request.data
            self.setState({ stateCopy })
        })
    }

	componentWillMount = () => {
		document.body.style.backgroundColor = "#FFFCC9";
        this.getData()
	}

	handleLoginBtnClick = () => {
		console.log(this.state.user)
	}
	
    render(){
        {console.log(this.state.user)}
		return(
			<div>
				<BaseContainer />
				<div id="body-navwrapper">
				  <div id="body-navbar">
					<div className="profile-paper">
                        <div className="title">
                            <label style={{fontFamily: 'lb_constantia'}} >User Account</label>
                        </div>
                        <div className="profile-photo">
                            <img className="photo" src={profileImage} />
                        </div>
                        <form className="profile-fields">
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Username:</label> <input className="text-box" type="text" name="lastname" value={this.state.user.username}/>
                            </div>
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Name:</label> <input className="text-box" type="text" name="lastname" value={this.state.user.name} />
                            </div>
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Email:</label> <input className="text-box" type="text" name="lastname" value={this.state.user.email} />
                            </div>
                            <div className="list">
                                <label style={{fontFamily: 'lb_constantia'}} className="text-label">Password:</label> <input className="text-box" type="text" name="lastname" value={this.state.user.password} />
                            </div>
                            <input type="button" value="Save" />  {/* alternative: <button /> */}
                        </form>
					</div>
				  </div>
				  </div>
		  </div>
        );
    }
}
