<p>交易通知，无Req属于私有流回报。</p>
<span class="anchor" id="22ec07ef-9a5d-43ce-91b6-4f6720d75dbd"></span>
## 1.函数原型
<p>virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {};</p>
<span class="anchor" id="77983f44-b44a-4315-8c8d-5dee0dcdd148"></span>
## 2.参数
<p>pTradingNoticeInfo：用户事件通知信息</p>
<pre><code>struct CThostFtdcTradingNoticeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///发送时间
    TThostFtdcTimeType SendTime;
    ///消息正文
    TThostFtdcContentType FieldContent;
    ///序列系列号
    TThostFtdcSequenceSeriesType SequenceSeries;
    ///序列号
    TThostFtdcSequenceNoType SequenceNo;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<span class="anchor" id="6e3bbf29-f47b-445f-b2e9-93c2e5fbbadc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e4e2c042-12c0-45c1-b2da-745573e99f15"></span>
## 4.FAQ
<p>无</p>
