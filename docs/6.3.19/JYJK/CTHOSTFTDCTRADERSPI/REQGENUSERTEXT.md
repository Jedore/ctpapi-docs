<p>用户发出获取短信验证码请求，暂不支持</p>
<p>响应: OnRspGenUserText</p>
<span class="anchor" id="688e47b1-d5c6-414b-844c-c8b0880035e5"></span>
## 1.函数原型
<p>virtual int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) = 0;</p>
<span class="anchor" id="caccdce0-6c0d-4ac2-93b8-badcee5d6941"></span>
## 2.参数
<p>pReqGenUserText：用户发出获取安全安全登陆方法请求</p>
<pre><code>struct CThostFtdcReqGenUserTextField
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
<span class="anchor" id="c091f89d-43fd-4cee-83bb-54c612bba9e7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2619e637-3f10-4982-9ff1-fb426cd9d199"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="bdb5dfb9-0d72-4a88-9027-1e1b6d65ba29"></span>
## 5.FAQ
<p>无</p>
