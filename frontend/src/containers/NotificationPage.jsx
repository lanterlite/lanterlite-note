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
import BaseContainer from './BaseContainer'

export default class BoardPage extends React.Component{

	componentWillMount = () => {
		document.body.style.backgroundColor = "#FFFCC9";
	}

    render(){
		return(
			<div>
			<BaseContainer/>

			</div>
        );
    }
}
