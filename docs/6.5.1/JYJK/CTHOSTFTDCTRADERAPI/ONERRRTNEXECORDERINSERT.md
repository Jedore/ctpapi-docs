<p>执行宣告录入错误回报，当执行ReqExecOrderInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="0b15aa6e-9ca2-4ee3-853a-57a2cb065dcc"></span>
## 1.函数原型
<p>virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="fdff5daf-3142-43d6-8eff-eee2b9fd6a39"></span>
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
<span class="anchor" id="18412945-cd7d-40be-bb57-17ad173fcb41"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2d15c341-60e6-42ae-ad30-0c3b606a2f16"></span>
## 4.FAQ
<p>无</p>
