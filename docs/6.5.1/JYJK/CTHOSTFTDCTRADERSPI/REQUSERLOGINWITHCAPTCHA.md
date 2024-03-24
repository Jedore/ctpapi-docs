<p>用户发出带有图片验证码的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="6206ae26-e777-463c-9950-7209bfc75f83"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithCaptcha(CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="589ed4e2-86ae-4455-b41a-5e779f133135"></span>
## 2.参数
<p>pReqUserLoginWithCaptcha：用户发出带图形验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithCaptchaField
{
///交易日
TThostFtdcDateType  TradingDay;
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///用户代码
TThostFtdcUserIDType    UserID;
///密码
TThostFtdcPasswordType  Password;
///用户端产品信息
TThostFtdcProductInfoType   UserProductInfo;
///接口端产品信息
TThostFtdcProductInfoType   InterfaceProductInfo;
///协议信息
TThostFtdcProtocolInfoType  ProtocolInfo;
///Mac地址
TThostFtdcMacAddressType    MacAddress;
///保留的无效字段
TThostFtdcOldIPAddressType  reserve1;
///登录备注
TThostFtdcLoginRemarkType   LoginRemark;
///图形验证码的文字内容
TThostFtdcPasswordType  Captcha;
///终端IP端口
TThostFtdcIPPortType    ClientIPPort;
///终端IP地址
TThostFtdcIPAddressType ClientIPAddress;
};
</code></pre>
<p>ClientIPAddress：填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="20e118dd-04fb-4289-9f0d-09d7726dd875"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b758b4d4-3223-4b54-b817-040a4f669962"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="88e7be6c-7487-4a6c-9660-1c427d3e354c"></span>
## 5.FAQ
<p>无</p>
