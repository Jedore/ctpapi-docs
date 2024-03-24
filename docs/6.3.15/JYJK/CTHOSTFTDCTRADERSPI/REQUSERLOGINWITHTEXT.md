<p>用户发出带有短信验证码的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="9976ec2a-ca48-4b3d-8c61-cb11ae1fcf92"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithText(CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID) = 0;</p>
<span class="anchor" id="1b36df6d-a676-4042-aa0f-aa724d2ffd31"></span>
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
<span class="anchor" id="849a877a-69d9-4ffc-a00e-d55314e6fb2a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="66bcf667-b369-4b31-96fe-d7b4ec051e1f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1526f530-27f4-40c4-b200-d8f99d2b995a"></span>
## 5.FAQ
<p>无</p>
