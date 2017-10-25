import React from 'react'
import PageHeader from '../components/base_components/Header'
// import SideBar from '../components/base_component/SideBar'

export default function BaseContainer(props){
	return (
		<div>
			<PageHeader />
			{/*
			{console.log(props)}
			<div className ="base">
				{props.children}
			</div>
			*/}
		</div>
	)
}
