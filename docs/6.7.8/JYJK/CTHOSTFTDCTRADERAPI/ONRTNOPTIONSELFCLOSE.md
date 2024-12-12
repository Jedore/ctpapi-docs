<p>期权自对冲通知，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="ce4e3aae-4605-4479-bb1b-2e7db24197e2"></span>
## 1.函数原型
<p>virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose) {};</p>
<span class="anchor" id="9a6ada57-0068-49c8-9506-49763d88c3f2"></span>
## 2.参数
<p>pOptionSelfClose：期权自对冲</p>
<pre><code>struct CThostFtdcOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///期权自对冲引用
    TThostFtdcOrderRefType  OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType  OptSelfCloseFlag;
    ///本地期权自对冲编号
    TThostFtdcOrderLocalIDType  OptionSelfCloseLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///期权自对冲提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType    NotifySequence;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///期权自对冲编号
    TThostFtdcOrderSysIDType    OptionSelfCloseSysID;
    ///报单日期
    TThostFtdcDateType  InsertDate;
    ///插入时间
    TThostFtdcTimeType  InsertTime;
    ///撤销时间
    TThostFtdcTimeType  CancelTime;
    ///自对冲结果
    TThostFtdcExecResultType    ExecResult;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///序号
    TThostFtdcSequenceNoType    SequenceNo;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType   UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType  StatusMsg;
    ///操作用户代码
    TThostFtdcUserIDType    ActiveUserID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType    BrokerOptionSelfCloseSeq;
    ///营业部编号
    TThostFtdcBranchIDType  BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType    CurrencyID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve3;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>InstallID：CTP内部使用</p>
<p>OrderSubmitStatus：报单报入状态</p>
<p>ExecResult：最后的结果，检查是否自对冲成功</p>
<p>StatusMsg：错误信息</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>ActiveUserID：委托回报报文中此字段值均为空，无论是否是首次委托其请求报文中此字段值也置为空。撤单回报报文中此字段值有值，同撤单请求报文。</p>
<span class="anchor" id="15a94b51-63b2-4e55-8119-cda6d27acf40"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b8187351-dc8b-45f0-8629-21ec236f7008"></span>
## 4.FAQ
<p>无</p>
