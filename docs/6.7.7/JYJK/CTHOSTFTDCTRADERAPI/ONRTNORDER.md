<p>报单通知，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="fa08ab72-bc70-4e79-a49e-71aec2afeeb9"></span>
## 1.函数原型
<p>virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {};</p>
<span class="anchor" id="060cba39-fcef-437e-9d2e-9ddf74e69491"></span>
## 2.参数
<p>pOrder：报单</p>
<pre><code>struct CThostFtdcOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///报单引用
    TThostFtdcOrderRefType  OrderRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///报单价格条件
    TThostFtdcOrderPriceTypeType    OrderPriceType;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///组合开平标志
    TThostFtdcCombOffsetFlagType    CombOffsetFlag;
    ///组合投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量
    TThostFtdcVolumeType    VolumeTotalOriginal;
    ///有效期类型
    TThostFtdcTimeConditionType TimeCondition;
    ///GTD日期
    TThostFtdcDateType  GTDDate;
    ///成交量类型
    TThostFtdcVolumeConditionType   VolumeCondition;
    ///最小成交量
    TThostFtdcVolumeType    MinVolume;
    ///触发条件
    TThostFtdcContingentConditionType   ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
    ///强平原因
    TThostFtdcForceCloseReasonType  ForceCloseReason;
    ///自动挂起标志
    TThostFtdcBoolType  IsAutoSuspend;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType  OrderLocalID;
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
    ///报单提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType    NotifySequence;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///报单编号
    TThostFtdcOrderSysIDType    OrderSysID;
    ///报单来源
    TThostFtdcOrderSourceType   OrderSource;
    ///报单状态
    TThostFtdcOrderStatusType   OrderStatus;
    ///报单类型
    TThostFtdcOrderTypeType OrderType;
    ///今成交数量
    TThostFtdcVolumeType    VolumeTraded;
    ///剩余数量
    TThostFtdcVolumeType    VolumeTotal;
    ///报单日期
    TThostFtdcDateType  InsertDate;
    ///委托时间
    TThostFtdcTimeType  InsertTime;
    ///激活时间
    TThostFtdcTimeType  ActiveTime;
    ///挂起时间
    TThostFtdcTimeType  SuspendTime;
    ///最后修改时间
    TThostFtdcTimeType  UpdateTime;
    ///撤销时间
    TThostFtdcTimeType  CancelTime;
    ///最后修改交易所交易员代码
    TThostFtdcTraderIDType  ActiveTraderID;
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
    ///用户强平标志
    TThostFtdcBoolType  UserForceClose;
    ///操作用户代码
    TThostFtdcUserIDType    ActiveUserID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType    BrokerOrderSeq;
    ///相关报单
    TThostFtdcOrderSysIDType    RelativeOrderSysID;
    ///郑商所成交数量
    TThostFtdcVolumeType    ZCETotalTradedVolume;
    ///互换单标志
    TThostFtdcBoolType  IsSwapOrder;
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
    ///报单回显字段
    TThostFtdcOrderMemoType OrderMemo;
    ///session上请求计数 api自动维护
    TThostFtdcSequenceNo12Type  SessionReqSeq;
};
</code></pre>
<p>ContingentCondition：作为条件单的触发条件</p>
<p>StopPrice：用户条件单的触发价格。</p>
<p>ForceCloseReason：投资者发出的报单请求填0“非强平”</p>
<p>InstallID：CTP内部使用</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>OrderSubmitStatus：CTP内部使用，普通投资者可以忽略</p>
<p>OrderStatus：报单状态</p>
<p>IsSwapOrder：是否互换单，是为1，否为0</p>
<p>InsertTime：状态为未知单时为ctp系统时间，从交易所返回后变更为交易所时间。</p>
<p><span alt="" id="anchor-id-03"></span> </p>
<p>OrderSource：报单来源：该字段由交易所返回的报文中取值，其他交易所有对应的取值，上期所较特殊，除交易所打回的报单以及秒成交的委托，其他的委托该字段为空</p>
<p>ActiveTraderID：是从交易所收回来，原值填写，CTP核心不处理该字段。在撤单回报中，由报单席位号修改为撤单席位号，以方便操作员在撤单回报中看出撤单是从哪个席位发起的。大商所该字段为空，上期所被交易所打回的报单以及秒成交的委托该字段也为空</p>
<p>BusinessUnit：是ctp内部使用字段，建议投资者不要使用</p>
<p>TraderID：是席位号</p>
<p>ActiveUserID：操作用户代码：一般只有撤单该字段才有值，其他情况一般为空</p>
<p>OrderType：报单类型，<a href="../../../qtywgz/bjhxj.html#anchor-id-02">报价中的情况</a></p>
<p><span alt="" id="anchor-id-02"></span> </p>
<p>ZCETotalTradedVolume：用于在郑商所分笔成交的时候返回总成交手数。</p>
<p>例：比如报入10手，一次性成交后并且是分笔成交的，会有多个<a href="../ONRTNTRADE/">OnRtnTrade</a>，一直到最后一个成交回报里才能收到traded=10，但是如果有zce这个字段，你可以在第一个分笔成交回报中就知道本次成交了几手。</p>
<p>CancelTime：对于交易所未返回撤单时间的委托，将排队机收到交易所撤单成功回报的时间作为撤单时间。目前中金所、大商所六期系统会返回撤单时间，上期所、能源中心、郑商所、大商所七期不返回撤单时间。</p>
<span class="anchor" id="09638ab6-77d3-4642-96ab-97e96568ba2d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9dcd0ffd-8a82-4fc0-9f87-6d947dbc2059"></span>
## 4.FAQ
<p><span alt="" id="anchor-id-10"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不同交易所，为什么InsertDate有的是自然日有的是交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>Insertdate字段，未知单、错单、上期所回报、能源回报、郑商所回报中该字段为自然日；大商所回报中为交易日。</p>
<p>建议确认一笔报单的时间用Tradingday+InsertTime这一组字段。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><span alt="" id="anchor-id-11"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">CTP是否支持单子挂起和激活回报的处理?如果其它柜台有此功能，CTP在收到这些回报能否有效处理，会不会引起系统问题?</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>交易所支持，ctp不支持，如果其他柜台对报单做挂起和激活操作，CTP支持未成交的挂单(OrderStatus=未成交不在队列中)， 不支持部分成交的挂单(OrderStatus= 部分成交不在队列中)</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
