<p>查询用户当前支持的认证模式，暂不支持</p>
<p>响应: OnRspUserAuthMethod</p>
<span class="anchor" id="c9e81fee-22b8-4750-92a2-45e91ba380df"></span>
## 1.函数原型
<p>virtual int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) = 0;</p>
<span class="anchor" id="7157a0bd-007c-4dbb-8bc1-09d1dc76e925"></span>
## 2.参数
<p>pReqUserAuthMethod：用户发出获取安全安全登陆方法请求</p>
<pre><code>struct CThostFtdcReqUserAuthMethodField
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
<span class="anchor" id="e9d46804-0b19-475d-8b91-1af853fd13ea"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="068609e1-1d4f-43ae-82b7-5d13c589a4ef"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="396d4120-9ba6-495e-ad69-ab05337f77bd"></span>
## 5.FAQ
<p>无</p>
