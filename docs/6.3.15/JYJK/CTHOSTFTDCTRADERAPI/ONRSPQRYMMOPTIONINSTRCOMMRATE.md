<p>请求查询做市商期权合约手续费响应，当执行ReqQryMMOptionInstrCommRate后，该方法被调用。</p>
<span class="anchor" id="bdd074bb-5c74-410f-b343-9360b6cf0500"></span>
## 1.函数原型
<p>virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="abe4afd3-45a9-4175-9e8d-0ebd668f6988"></span>
## 2.参数
<p>pMMOptionInstrCommRate：当前做市商期权合约手续费的详细内容</p>
<pre><code>struct CThostFtdcMMOptionInstrCommRateField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///开仓手续费率
    TThostFtdcRatioType OpenRatioByMoney;
    ///开仓手续费
    TThostFtdcRatioType OpenRatioByVolume;
    ///平仓手续费率
    TThostFtdcRatioType CloseRatioByMoney;
    ///平仓手续费
    TThostFtdcRatioType CloseRatioByVolume;
    ///平今手续费率
    TThostFtdcRatioType CloseTodayRatioByMoney;
    ///平今手续费
    TThostFtdcRatioType CloseTodayRatioByVolume;
    ///执行手续费率
    TThostFtdcRatioType StrikeRatioByMoney;
    ///执行手续费
    TThostFtdcRatioType StrikeRatioByVolume;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="326dd73e-1c89-420c-927e-8f9324486090"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0ee255ab-5367-48f1-be27-ce21ee05d5aa"></span>
## 4.FAQ
<p>无</p>
