<p>用户发出带有动态口令的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="9a81cc77-2b98-4c92-ab6c-48c864425033"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) = 0;</p>
<span class="anchor" id="6a84cf8e-f906-46ab-bcb0-9ca89ec4aa26"></span>
## 2.参数
<p>pReqUserLoginWithOTP：用户发出带动态验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithOTPField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///密码
    TThostFtdcPasswordType Password;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///接口端产品信息
    TThostFtdcProductInfoType InterfaceProductInfo;
    ///协议信息
    TThostFtdcProtocolInfoType ProtocolInfo;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///终端IP地址
    TThostFtdcIPAddressType ClientIPAddress;
    ///登录备注
    TThostFtdcLoginRemarkType LoginRemark;
    ///OTP密码
    TThostFtdcPasswordType OTPPassword;
    ///终端IP端口
    TThostFtdcIPPortType ClientIPPort;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="13ad511c-480d-4c30-bdde-8bd56752b3a2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="22bbd575-a29e-4e8c-9ea3-97e67bfe7a50"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="16e48d49-cec5-41c7-bb38-434a961985ce"></span>
## 5.FAQ
<p>无</p>
