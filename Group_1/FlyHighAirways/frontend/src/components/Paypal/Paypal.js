import React, { Component } from 'react'

import PayPalExpressBtn from 'react-paypal-express-checkout';
import { withRouter } from 'react-router-dom';

import axios from 'axios';

class Paypal extends Component {
    render() {


        const makeid = (length) => {
            var result           = '';
            var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            var charactersLength = characters.length;
            for ( var i = 0; i < length; i++ ) {
               result += characters.charAt(Math.floor(Math.random() * charactersLength));
            }
            return result;
        }
         

        const onSuccess = (payment) => {

            const makePaymentData = {
                referenceString: makeid(8),
                amount: parseInt(this.props.toPay)
            }


            axios.post('http://localhost:5000/book/make-payment', makePaymentData, {
                headers: {
                    // 'Authorization': `Bearer ${this.props.bookingData.auth.idToken}`,
                    'Content-Type': 'application/json'
                }
            })
            .then(res => {

                const flightData = {
                    flightNumber: this.props.bookingData.id,
                    passengers: this.props.passengers,
                    paymentReferenceKey: makePaymentData.referenceString,
                    date: '2019-05-06'
                }

                console.log(this.props.passengers);

                axios.post('http://localhost:5000/book/book-flight', flightData, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(res => {
                    console.log('book flight response',res.data);
                })
                .catch(err => {
                    console.log(err);
                })
            })

            this.props.history.push('/')
        }

        const onCancel = (data) => {
            console.log(JSON.stringify(data));
        }

        const onError = (err) => {
            console.log(JSON.stringify(err));
        }

        let env = 'sandbox';
        let currency = 'USD';
        let total = parseInt(this.props.toPay * 0.01368);
        console.log(total);

        const client = {
            sandbox: 'AeCP7XjbY68kPoHkF4cqS2LWBZ83t1wSFRy6jbEdbGFG4c_m3qI6j_qozn84D8xpTN3ML6opD6XanSgO',
            production: ''
        }


        return (
            <div>
                <PayPalExpressBtn 
                    env={env}
                    client={client}
                    currency={currency}
                    total={total}
                    onError={onError}
                    onSuccess={onSuccess}
                    onCancel={onCancel}
                    style={{
                        size: 'large',
                        shape: 'rect',
                        label: 'checkout'
                    }}
                />
            </div>
        )
    }
}


export default withRouter(Paypal)