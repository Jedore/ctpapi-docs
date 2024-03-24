<p>用户发出获取图形验证码请求，暂不支持</p>
<p>响应: OnRspGenUserCaptcha</p>
<span class="anchor" id="88d2c6cf-1a7b-4bb6-bc54-d3a96d312634"></span>
## 1.函数原型
<p>virtual int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="5b13f8b5-34df-4c24-b8c9-e685be230934"></span>
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
<span class="anchor" id="59735bc2-8829-433c-85fd-66ee78d41fd3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d0b7a81c-9163-4845-9989-c09c0731574f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="3aa66dee-bf86-4f43-8be6-1a4814e087cc"></span>
## 5.FAQ
<p>无</p>
