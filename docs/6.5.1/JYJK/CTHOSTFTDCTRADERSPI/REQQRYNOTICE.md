<p>请求查询客户通知</p>
<p>响应: OnRspQryNotice</p>
<span class="anchor" id="4802db17-dd54-4121-a603-a261f462dce0"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="62629f2d-887d-4e13-9a19-a62574df7fba"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="bd428318-67a2-4f13-aca0-c15c77763faa"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1be642bc-98be-4070-82ef-22c69694b484"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c1aba640-0322-4946-b604-0b3cf9589ee1"></span>
## 5.FAQ
<p>无</p>
