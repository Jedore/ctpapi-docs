<p>用户发出带有图片验证码的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="fc366d3a-bdcf-4986-82ab-063c8a34cc16"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="37d1210b-0a4d-4f7c-8250-1b4e8af1e2aa"></span>
## 2.参数
<p>pReqUserLoginWithCaptcha：用户发出带图形验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithCaptchaField
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
    ///图形验证码的文字内容
    TThostFtdcPasswordType Captcha;
    ///终端IP端口
    TThostFtdcIPPortType ClientIPPort;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="c06b979c-e48f-4117-80ac-915775434edf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ce3b38e4-a8db-4bed-9780-07df7d555f4b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5faa9185-1e4f-4cce-b637-487dec9d8dfe"></span>
## 5.FAQ
<p>无</p>
