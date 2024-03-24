<p>用户发出获取图形验证码请求，暂不支持</p>
<p>响应: OnRspGenUserCaptcha</p>
<span class="anchor" id="4d96f7ca-5748-4442-adf2-7c0672f2f740"></span>
## 1.函数原型
<p>virtual int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="63d200af-bf0c-4d10-b590-508a29f0ff2c"></span>
## 2.参数
<p>pReqGenUserCaptcha：用户发出获取安全安全登陆方法请求</p>
<pre><code>struct CThostFtdcReqGenUserCaptchaField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4fca896e-6889-4928-a4ce-a5847f0db0d3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cdb7ce54-ad2b-4ded-9b5b-c9ed8e53b85e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="fa403b1e-9e0f-4f45-acb9-ad15bfbc81d8"></span>
## 5.FAQ
<p>无</p>
