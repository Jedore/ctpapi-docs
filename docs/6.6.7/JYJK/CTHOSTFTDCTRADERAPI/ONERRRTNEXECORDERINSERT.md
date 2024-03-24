<p>执行宣告录入错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="f6c57bc3-1278-4f48-b5a4-a1f3ab10dc5f"></span>
## 1.函数原型
<p>virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="f3096cde-232e-4223-9229-339312a398e2"></span>
## 2.参数
<p>pInputExecOrder：输入的执行宣告</p>
<pre><code>struct CThostFtdcInputExecOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///执行宣告引用
    TThostFtdcOrderRefType  ExecOrderRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///开平标志
    TThostFtdcOffsetFlagType    OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///执行类型
    TThostFtdcActionTypeType    ActionType;
    ///保留头寸申请的持仓方向
    TThostFtdcPosiDirectionType PosiDirection;
    ///期权行权后是否保留期货头寸的标记,该字段已废弃
    TThostFtdcExecOrderPositionFlagType ReservePositionFlag;
    ///期权行权后生成的头寸是否自动平仓
    TThostFtdcExecOrderCloseFlagType    CloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType    CurrencyID;
    ///交易编码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="40aed4a7-407b-44f4-89dd-293b5a8ddc52"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0275af4a-41aa-4e9d-81b5-65d19afa09a8"></span>
## 4.FAQ
<p>无</p>
