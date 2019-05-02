
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react'
import './snacks.css';
import { Link } from "react-router-dom"


export class Snacks extends Component {
    render() {
        return (

            <div className='backgroundsnacks'>
                <div className='container-fluid' >
                    <div className='row'>
                        <div className='col-sm-8' style={{ paddingLeft: '5%', paddingRight: '5%' }}>

                            <div className='headerimg'>
                                <img src='//in.bmscdn.com/bmsin/fnb/offerbanner/web/web-offerbanner.jpg' style={{ width: '93%', height: "auto", maxWidth: 'inherit' }} />
                            </div>


                            <div className='snacksbody' >
                                <div className='container' maxWidth='inherit'>
                                    <div className='row '>
                                        <div className='col-sm-12 snackshead'>
                                            <p className='snackshead1'> Grab a <span style={{ color: 'red' }}>Bite!</span></p>
                                            <p className='snackshead2'> Prebook Your Meal and <span style={{ color: 'red' }}>save more!</span></p>
                                        </div>
                                    </div>
                                    <div className='row '>
                                        <div className='col-sm-12 snackslist'>
                                            <div className="card " style={{ width: '30%' }}>
                                                <img className="card-img-top" src="//in.bmscdn.com/bmsin/v2/Web-v2/d-combo/1020006_06082018135441.jpg" alt="Card image" style={{ width: '100 %', height: 'fit-content' }} />
                                                <div className="card-body">
                                                    <h6 className="card-title" >John Doe</h6>
                                                    <p className="card-text">Some example </p>
                                                </div>
                                            </div>
                                            <div className="card " style={{ width: '30%' }}>
                                                <img className="card-img-top" src="//in.bmscdn.com/bmsin/v2/Web-v2/d-combo/1020006_06082018135441.jpg" alt="Card image" style={{ width: '100 %', height: 'fit-content' }} />
                                                <div className="card-body">
                                                    <h6 className="card-title" >John Doe</h6>
                                                    <p className="card-text">Some example </p>
                                                </div>
                                            </div>
                                            <div className="card " style={{ width: '30%' }}>
                                                <img className="card-img-top" src="//in.bmscdn.com/bmsin/v2/Web-v2/d-combo/1020006_06082018135441.jpg" alt="Card image" style={{ width: '100 %', height: 'fit-content' }} />
                                                <div className="card-body">
                                                    <h6 className="card-title" >John Doe</h6>
                                                    <p className="card-text">Some example </p>
                                                </div>
                                            </div>



                                        </div>
                                    </div>
                                    <div className='row '>
                                        <div className='col-sm-12 snacksfooter'>
                                            Note:
                                        <ol style={{ fontSize: 'small' }}>
                                                <li>Images are for representation purposes only</li>
                                                <li>Prices inclusive of taxes</li>
                                            </ol>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>


                        <div className='col-sm-4'>

                            <div className='bookingsummary'>

                                <div className='bookingsummaryrates'>
                                    <table width='100%' >
                                        <tr>
                                            <td style={{ padding: '16px', color: 'aliceblue' }}> <span style={{ fontSize1: '16px' }}>PH 67,68<span style={{ fontSize1: '12px' }}>(2 tickets)</span></span></td>
                                            <td style={{ textAlign: 'right', padding: '16px', color: 'aliceblue' }}>  Rs 300/-</td>
                                        </tr>
                                        <tr>
                                            <td> Internet handling charges</td>
                                            <td style={{ textAlign: 'right', padding: '16px', color: 'aliceblue' }}>Rs 20/-</td>
                                        </tr>
                                    </table>
                                </div>
                                <div className='bookingsummarytotalamount'>
                                    <table width='100%' >
                                        <tr>
                                            <td> <span style={{ fontSize1: '18px', padding: '16px', color: 'aliceblue' }}>Sub total</span></td>
                                            <td style={{ textAlign: 'right', padding: '16px', color: 'aliceblue' }}>  Rs 320/-</td>
                                        </tr>

                                    </table>
                                </div>
                                <div className='bookingsummarysubmit'>
                                    <button type="button" class="btn btn-danger btn-block">Pay</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div >


        )
    }
}

export default Snacks;
