<p>请求查询交易通知</p>
<p>响应: OnRspQryTradingNotice</p>
<span class="anchor" id="1bfee356-1431-4726-8f0b-51edd2f68cc7"></span>
## 1.函数原型
<p>virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;</p>
<span class="anchor" id="f12c4fad-1b77-4b3d-a95b-ffeeb220a628"></span>
## 2.参数
<p>pQryTradingNotice：查询交易事件通知</p>
<pre><code>struct CThostFtdcQryTradingNoticeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="897d61f8-01a6-4bf6-bd05-2746f7dad139"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8d22dd3b-0de5-4914-be3a-19ba1b6d55a5"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5936c522-a899-43c6-bd7b-8531c2eb773c"></span>
## 5.FAQ
<p>无</p>
