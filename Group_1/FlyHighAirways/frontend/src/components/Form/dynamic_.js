import React, { Component } from "react";
import { Form, Input, InputNumber, Icon, Button, Select, Row, Col } from "antd";
const { Option } = Select;

let id = 0;

class DynamicFieldSet extends React.Component {
  remove = k => {
    const { form } = this.props;
    // can use data-binding to get
    const keys = form.getFieldValue("keys");
    // We need at least one passenger
    if (keys.length === 1) {
      return;
    }

    // can use data-binding to set
    form.setFieldsValue({
      keys: keys.filter(key => key !== k)
    });

    this.props.onAdd(keys.length - 1);
  };

  add = () => {
    const { form } = this.props;
    // can use data-binding to get
    const keys = form.getFieldValue("keys");
    const nextKeys = keys.concat(id++);
    // can use data-binding to set
    // important! notify form to detect changes
    form.setFieldsValue({
      keys: nextKeys
    });
    this.props.onAdd(keys.length + 1);
  };

  handleSubmit = e => {
    e.preventDefault();
    this.props.onSubmit()
    this.props.form.validateFields((err, values) => {
      if (!err) {
        // const { keys, names } = values;
        // console.log("Received values of form: ", values);
        // console.log("Merged values:", keys.map(key => names[key]));
      }
    });
  };

  render() {

    const { getFieldDecorator, getFieldValue } = this.props.form;
    const formItemLayout = {
      labelCol: {
        // xs: { span: 4 },
        // sm: { span: 4 }
      },
      wrapperCol: {
        // xs: { span: 24 },
        // sm: { span: 20 }
      }
    };
    const formItemLayoutWithOutLabel = {
      wrapperCol: {
        // xs: { span: 24, offset: 0 },
        // sm: { span: 20, offset: 4 }
      }
    };
    getFieldDecorator("keys", { initialValue: [] });
    const keys = getFieldValue("keys");
    const formItems = keys.map((k, index) => (
      //   <Form.Item {...formItemLayout} label="Name">
      //   {getFieldDecorator("username", {
      //     rules: [
      //       {
      //         required: true,
      //         message: "Please input your name"
      //       }
      //     ]
      //   })(<Input placeholder="Please input your name" />)}
      // </Form.Item>
      <React.Fragment key={`${k}-name`}>
        <Row>
          <Col lg={10}>
            <Form.Item
              {...(index === 0 ? formItemLayout : formItemLayoutWithOutLabel)}
              label={index === 0 ? "Passengers" : ""}
              required={false}
              
            >
              {getFieldDecorator(`passengers[${k}].name`, {
                validateTrigger: ["onChange", "onBlur"],
                rules: [
                  {
                    required: true,
                    whitespace: true,
                    message:
                      "Please input passenger's name or delete this field."
                  }
                ]
              })(
                <Input
                  placeholder="passenger name"
                  style={{ width: "80%", marginRight: 8 }}
                />
              )}
              {/* {keys.length > 1 ? (
                <Icon
                  className="dynamic-delete-button"
                  type="minus-circle-o"
                  disabled={keys.length === 1}
                  onClick={() => this.remove(k)}
                />
              ) : null} */}
            </Form.Item>
          </Col>
          <Col lg={10}>
            <Form.Item
              {...(index === 0 ? formItemLayout : formItemLayoutWithOutLabel)}
              label={index === 0 ? "Passengers" : ""}
              required={false}
              key={`${k}-email`}
            >
              {getFieldDecorator(`passengers[${k}].email`, {
                validateTrigger: ["onChange", "onBlur"],
                rules: [
                  {
                    required: true,
                    whitespace: true,
                    message:
                      "Please input passenger's email or delete this field."
                  }
                ]
              })(
                <Input
                  placeholder="passenger Email"
                  style={{ width: "90%", marginRight: 8 }}
                />
              )}
              {keys.length > 1 ? (
                <Icon
                  className="dynamic-delete-button"
                  type="minus-circle-o"
                  disabled={keys.length === 1}
                  onClick={() => this.remove(k)}
                />
              ) : null}
            </Form.Item>
          </Col>
        </Row>
      </React.Fragment>
    ));
    return (
      <Form onSubmit={this.handleSubmit}>
        {formItems}
        <Form.Item {...formItemLayoutWithOutLabel}>
          <Button type="dashed" onClick={this.add} style={{ width: "60%" }}>
            <Icon type="plus" /> Add field
          </Button>
        </Form.Item>

        <Form.Item {...formItemLayoutWithOutLabel}>
          <Button 
              type="primary" 
              htmlType="submit"
              disabled={!(this.props.isFlightSelected[0] !== null && this.props.isFlightSelected[1] > 0)}    
          >
            Submit
          </Button>
        </Form.Item>
      </Form>
    );
  }
}

export default DynamicFieldSet;

// const WrappedDynamicFieldSet = Form.create({ name: "dynamic_form_item" })(
//   DynamicFieldSet
// );

// React.render(<WrappedDynamicFieldSet />);
