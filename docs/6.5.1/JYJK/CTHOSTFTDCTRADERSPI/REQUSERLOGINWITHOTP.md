<p>用户发出带有动态口令的登陆请求，暂不支持</p>
<p>响应: OnRspUserLogin</p>
<span class="anchor" id="d8229bbc-740a-47e1-8211-2f01854cee2a"></span>
## 1.函数原型
<p>virtual int ReqUserLoginWithOTP(CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID) = 0;</p>
<span class="anchor" id="41c33901-4b21-406b-b75a-07e61155d3bf"></span>
## 2.参数
<p>pReqUserLoginWithOTP：用户发出带动态验证码的登录请求请求</p>
<pre><code>struct CThostFtdcReqUserLoginWithOTPField
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
    ///OTP密码
    TThostFtdcPasswordType  OTPPassword;
    ///终端IP端口
    TThostFtdcIPPortType    ClientIPPort;
    ///终端IP地址
    TThostFtdcIPAddressType ClientIPAddress;
};
</code></pre>
<p>ClientIPAddress：填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="12092718-7f22-4e09-ab28-055e30211ff3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4c0a9bc4-12a9-4b26-a62a-51fbcbb6935b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ed6a6f14-209a-4600-a549-fb3a54265073"></span>
## 5.FAQ
<p>无</p>
