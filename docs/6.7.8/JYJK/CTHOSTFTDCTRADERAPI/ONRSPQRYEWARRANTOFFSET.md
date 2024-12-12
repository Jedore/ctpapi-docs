<p>请求查询仓单折抵信息响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEWARRANTOFFSET/">ReqQryEWarrantOffset</a>后，该方法被调用。</p>
<span class="anchor" id="76f8b95c-8b17-44e1-bbb2-cb56a0f99dd5"></span>
## 1.函数原型
<p>virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f333ba10-58c1-4d2d-8cd7-b61f04fe586b"></span>
## 2.参数
<p>pEWarrantOffset：仓单折抵信息</p>
<pre><code>struct CThostFtdcEWarrantOffsetField
{
    ///交易日期
    TThostFtdcTradeDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///数量
    TThostFtdcVolumeType    Volume;
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
<span class="anchor" id="53c11531-1951-4129-a968-97a3ba15616e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b71ca88e-0055-414a-b3e6-94f61de1fa6b"></span>
## 4.FAQ
<p>无</p>
