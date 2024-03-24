<p>请求查询投资者持仓明细，对应响应OnRspQryInvestorPositionDetail。</p>
<p>CTP系统根据来自交易所的成交记录生成持仓明细记录，一笔成交记录对应一条持仓明细记录。</p>
<span class="anchor" id="47c83502-b859-4661-9ffd-1ef749252719"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) = 0;</p>
<span class="anchor" id="c6e949d9-c6ed-4d9e-aeab-a4bc8a58c441"></span>
## 2.参数
<p>pQryInvestorPositionDetail：查询投资者持仓明细</p>
<pre><code>struct CThostFtdcQryInvestorPositionDetailField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="87bde641-d772-42aa-aadd-b55959ba5f75"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f05793d8-8c7d-4a52-80d0-e9a67b5e8ad2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1d03117d-00fa-4db7-a04a-0eccd3f6cffa"></span>
## 5.FAQ
<p>无</p>
