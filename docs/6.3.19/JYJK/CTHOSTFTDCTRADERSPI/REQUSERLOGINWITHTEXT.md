<p>用户发出带有短信验证码的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="b5117bef-1c24-4813-9576-7393cbd394a8"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithText(CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID) = 0;</p>
<span class="anchor" id="a5e3bf2c-7244-4cad-a8a8-412e6188005d"></span>
## 2.参数
<p>pReqUserLoginWithText：用户发出带短信验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithTextField
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
    ///短信验证码文字内容
    TThostFtdcPasswordType Text;
    ///终端IP端口
    TThostFtdcIPPortType ClientIPPort;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="c11eb3bc-c399-43f5-ac5c-1be61eb44086"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3a22fb1f-398c-4123-a511-8d101dcfb302"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="19273475-73f6-4545-85b7-8a5e1a08f0b6"></span>
## 5.FAQ
<p>无</p>
