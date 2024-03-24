<p>请求查询期权合约手续费响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRCOMMRATE/">ReqQryOptionInstrCommRate</a>后，该方法被调用。</p>
<span class="anchor" id="b6dda02c-c83b-46f7-982c-f053ac661f1c"></span>
## 1.函数原型
<p>virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="23d65658-2b7a-4a48-8416-4d112bc381ab"></span>
## 2.参数
<p>pOptionInstrCommRate：当前期权合约手续费的详细内容</p>
<pre><code>struct CThostFtdcOptionInstrCommRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
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
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="00dd4f2d-980d-4699-b27c-c19e5bec30c1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c324f037-de3f-4992-9a70-a99b69efd8bc"></span>
## 4.FAQ
<p>无</p>
