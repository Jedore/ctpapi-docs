<p>用户发出获取短信验证码请求，暂不支持</p>
<p>响应: OnRspGenUserText</p>
<span class="anchor" id="13f73d6e-711b-461e-8487-52b2726642ca"></span>
## 1.函数原型
<p>virtual int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) = 0;</p>
<span class="anchor" id="eae38722-edc4-4275-8791-d59639a5d33b"></span>
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
<span class="anchor" id="b7b711d6-4a0a-4fe0-8753-a702936c7962"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0278e418-ec71-401b-8091-4e88868e6fb4"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a4d9326a-11d8-4db8-a92a-fcdc01863e0a"></span>
## 5.FAQ
<p>无</p>
