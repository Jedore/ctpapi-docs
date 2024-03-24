<p>请求查询交易通知</p>
<p>响应: OnRspQryTradingNotice</p>
<span class="anchor" id="0b96412d-5657-4a01-934a-3be2b64a91c0"></span>
## 1.函数原型
<p>virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;</p>
<span class="anchor" id="38c6cc1b-0c0d-4b57-b8f2-1c524cf9b776"></span>
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
<span class="anchor" id="e030f8f7-ab90-4134-a122-a4187136bc47"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c20ae52e-dea5-41a7-8c2e-c09280cc0d74"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0ecafd9d-3689-4eb8-baab-cc30fb7c3d72"></span>
## 5.FAQ
<p>无</p>
