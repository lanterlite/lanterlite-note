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

export default class LoginPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            settings:{
                showEditButton: true,
                showDoneButton: false,
                disableEditText: false,
                isRedirect: false,
            },
            deleteState:{
                openDialog: false,
            },
            uploadState:{
                openDialog:false,
                uploadedFile: null,
				isUploaded: false,
            },
            saveState:{
                openDialog: false,
            },
      };
    }
	
	componentWillMount = () => {
		document.body.style.backgroundColor = "#FFFCC9";
	}

	handleLoginBtnClick = () => {
		console.log(this.state.user)
	}
	
    render(){
		return(
			<div>
				<div id="navwrapper">
				  <div id="navbar">
	  				<ul id="navbar-ul">
						<form className="login-form">
							<input id="inputtext" type="text" name="lastname" placeholder="Email" />
							<input id="inputtext" type="text" name="lastname" placeholder="Password" />
							<input id="login-button" onClick={this.handleLoginBtnClick} type="button" value="Login" />	{/* alternative: <button /> */}
						</form>
					</ul>				 
				  </div>
				  </div>


				<div id="body-navwrapper">
				  <div id="body-navbar">
					<div className="login-title">
						<label style={{fontFamily: 'lb_constantia', fontSize: 70}}>Liteboard</label>
					</div>
					<form className="signup-form">
						<input type="text" name="lastname" placeholder="Email" />
						<input type="text" name="lastname" placeholder="Password" />
						<input type="text" name="lastname" placeholder="Confirm Password" />
						{/*
						<RaisedButton 
							onClick={this.handleLoginBtnClick}
							type="button" 
							value="Sign Up"
						/>
					*/}
						<input onClick={this.handleLoginBtnClick} type="button" value="Sign Up" />	{/* alternative: <button /> */}
					</form>
				  </div>
				  </div>
			</div>
        );
    }
}
