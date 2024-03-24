<p>请求RCAMS策略组合持仓查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINVESTORCOMBPOSITION/">ReqQryRCAMSInvestorCombPosition</a>后，该方法被调用。</p>
<span class="anchor" id="a28549b9-0f33-4b35-b8d1-f633333ecd46"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInvestorCombPosition(CThostFtdcRCAMSInvestorCombPositionField *pRCAMSInvestorCombPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9f0ada3e-ecdc-4305-b890-9af9964d7dd2"></span>
## 2.参数
<p>pRCAMSInvestorCombPosition：RCAMS策略组合持仓</p>
<pre><code>struct CThostFtdcRCAMSInvestorCombPositionField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///投套标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///持仓多空方向
    TThostFtdcPosiDirectionType PosiDirection;
    ///组合合约代码
    TThostFtdcInstrumentIDType  CombInstrumentID;
    ///单腿编号
    TThostFtdcLegIDType LegID;
    ///交易所组合合约代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///持仓量
    TThostFtdcVolumeType    TotalAmt;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///投资者保证金
    TThostFtdcMoneyType Margin;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="9e04bb1d-3daa-4ebe-894e-aa7ef6880b27"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a016fc9b-cd52-4d75-b4b6-8f14ec3b9d8b"></span>
## 4.FAQ
<p>无</p>
