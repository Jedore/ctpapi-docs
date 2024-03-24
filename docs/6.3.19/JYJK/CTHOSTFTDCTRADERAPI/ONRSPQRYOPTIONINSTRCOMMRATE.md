<p>请求查询期权合约手续费响应，当执行ReqQryOptionInstrCommRate后，该方法被调用。</p>
<span class="anchor" id="d6114ba4-23d8-4931-a15f-1d4f831954ee"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="54d53902-f62f-4c51-b3e7-e7beba3e86bd"></span>
## 2.参数
<p>pOptionInstrCommRate：当前期权合约手续费的详细内容</p>
<pre><code>struct CThostFtdcOptionInstrCommRateField
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
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="453fe8e0-b17c-4f85-844c-f8a38b612b01"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="20a8c6c2-fa43-4711-8457-336d12223d41"></span>
## 4.FAQ
<p>无</p>
